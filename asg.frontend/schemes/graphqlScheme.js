import { gql } from 'graphql-tag'

import { LocalScheme } from '~auth/runtime'

const LOGIN_MUTATION = gql`
  mutation tokenAuth($email: String, $password: String) {
    tokenAuth(email: $email, password: $password) {
      success
      errors
      token
      refreshToken
      unarchiving
      user {
        id
        username
      }
    }
  }
`

// export const LOGOUT_MUTATION = gql`
//   mutation LogOutMutation {
//     logOut
//   }
// `

export const USER_DETAILS_QUERY = gql`
  query UserDetailsQuery {
    me {
      username
      verified
    }
  }
`




export default class GraphQLScheme extends LocalScheme {
  async login(credentials, { reset = true } = {}) {
    console.log(credentials)
    const {
      apolloProvider: { defaultClient: apolloClient },
      $apolloHelpers,
    } = this.$auth.ctx.app
  
    // Ditch any leftover local tokens before attempting to log in
    if (reset) {
      this.$auth.reset({ resetInterceptor: false })
    }
  
    // Make login request
    const response = await apolloClient
      .mutate({
        mutation: LOGIN_MUTATION,
        variables: credentials,
      })
      .then(({ data }) => data && data.tokenAuth)
      .catch((errors) => {
        console.log(errors)
        console.log(1)
      })
    
    // Update our cookie token
    console.log(response);
    this.token.set(response.token)
  
    // Set our graphql-token so subsequent graphql request are authenticated
    await $apolloHelpers.onLogin(response.token)
  
    // Fetch user
    await this.fetchUser() // We will define this function next
  
    return response.token
  }

  fetchUser() {
    const {
      apolloProvider: { defaultClient: apolloClient },
    } = this.$auth.ctx.app
  
    // Token is required but not available
    if (!this.check().valid) {
      return
    }
  
    // Try to fetch user
    return apolloClient
      .query({
        query: USER_DETAILS_QUERY,
      })
      .then(({ data }) => {
        if (!data.me) {
          const error = new Error(`User Data response not resolved`)
          return Promise.reject(error)
        }
        // Set the auth user
        this.$auth.setUser(data.me)
  
        return data.me
      })
      .catch((error) => {
        this.$auth.callOnError(error, { method: 'fetchUser' })
        return Promise.reject(error)
      })
  }

  // async logout() {
  //   const {
  //     apolloProvider: { defaultClient: apolloClient },
  //     $apolloHelpers,
  //   } = this.$auth.ctx.app
  
  //   await apolloClient
  //     .mutate({
  //       mutation: LOGOUT_MUTATION,
  //     })
  //     .catch(() => {
  //       // Handle errors
  //     })
  
  //   // Reset regardless
  //   $apolloHelpers.onLogout()
  //   return this.$auth.reset({ resetInterceptor: false })
  // }

  initializeRequestInterceptor() {
    // Instead of initializing axios interceptors, Do nothing
    // Since we are not using axios
  }

  reset() {
    this.$auth.setUser(false)
    this.token.reset()
  }
}
