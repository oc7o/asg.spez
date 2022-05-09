<template>
  <b-navbar type="is-primary">
    <template #brand>
      <b-navbar-item
        tag="router-link"
        :to="{ path: '/' }"
        style="background-color: #f4f2e1"
      >
        <img :src="require(`~/assets/spezi.png`)" />
      </b-navbar-item>
    </template>
    <template #start>
      <b-navbar-item href="/"> Home </b-navbar-item>

      <template v-for="category in allCategories">
        <b-navbar-dropdown :key="category.slug" v-if="category.inNavbar" :label="category.title">
          <b-navbar-item v-for="subpage in category.pages" :key="subpage.slug" :href="`/${category.slug}/${subpage.slug}`"> {{ subpage.title }} </b-navbar-item>
        </b-navbar-dropdown>
      </template>

      <template v-for="page in allPages">
        <b-navbar-item :key="page.slug" v-if="page.inNavbar" :href="`/${page.slug}`"> {{ page.title }} </b-navbar-item>
      </template>
    </template>

    <template #end>
      <b-navbar-item tag="div">
        <div class="buttons">
          <a class="button is-success" @click="cardModal"> Log in </a>
        </div>
      </b-navbar-item>
    </template>
  </b-navbar>
</template>

<script>
import gql from 'graphql-tag'
import LoginModal from '@/components/LoginModal.vue'

export default {
  apollo: {
    allPages: gql`
      query {
        allPages {
          title
          slug
          inNavbar
        }
      }
    `,
    allCategories: gql`
    query {
      allCategories {
        title
        slug
        inNavbar
        pages {
          title
          slug
        }
      }
    }
    `
  },
  methods: {
    cardModal() {
      this.$buefy.modal.open({
        parent: this,
        component: LoginModal,
        hasModalCard: true,
        trapFocus: true,
      })
    },
  },
}
</script>
