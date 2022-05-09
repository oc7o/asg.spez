import { gql } from 'graphql-tag'

import { LocalScheme } from '~auth/runtime'

const LOGIN_MUTATION = gql`
  mutation LoginMutation($email: String, $password: String) {
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
  // TODO: Override relevant LocalScheme methods
}
