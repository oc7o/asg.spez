<template>
  <div>
     <section class="section is-medium" v-if="pageBySlug.category == null" v-html="content"></section>
  </div>
</template>
<script>
import gql from 'graphql-tag'

export default {
  apollo: {
    pageBySlug: {
      query: gql`
       query pageBySlug($slug: String) {
        pageBySlug(slug: $slug) {
          title
          slug
          inNavbar
          category {
            slug
            title
          }
          content
        }
      }
      `,
      variables() {
        return {
          slug: this.$route.params.slug1,
        }
      },
    },
  },
  data () {
    return {}
  },
  computed: {
    content () {
      return this.$content(this.pageBySlug.content)
    }
  }
}
</script>
<style scoped>

</style>