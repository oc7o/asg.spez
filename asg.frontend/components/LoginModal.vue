<template>
  <form action="">
    <div class="modal-card" style="width: auto">
      <header class="modal-card-head">
        <p class="modal-card-title">Login</p>
        <button type="button" class="delete" @click="$emit('close')" />
      </header>
      <section class="modal-card-body">
        <b-field label="Email">
          <b-input
            type="email"
            :value="loginForm.email"
            placeholder="Your email"
            required
            v-model="loginForm.email"
          >
          </b-input>
        </b-field>
        <b-field label="Password">
          <b-input
            type="password"
            :value="loginForm.password"
            password-reveal
            placeholder="Your password"
            required
            v-model="loginForm.password"
          >
          </b-input>
        </b-field>
      </section>
      <footer class="modal-card-foot">
        <b-button label="Close" @click="$emit('close')" />
        <b-button label="Login" type="is-primary" @click="handleLoginSubmit" />
      </footer>
    </div>
  </form>
</template>
<script>
export default {
  data() {
    return {
      loginForm: {
        email: '',
        password: '',
      },
      formBusy: false,
    }
  },
  methods: {
    async handleLoginSubmit() {
      const credentials = this.loginForm
      this.formBusy = true

      try {
        // Using our custom strategy 
        await this.$auth.loginWith('graphql', credentials)

        this.formBusy = false
      } catch (errors) {
        this.formBusy = false
        console.log(errors)
        // Handle errors
      }
    },
  },
}
</script>