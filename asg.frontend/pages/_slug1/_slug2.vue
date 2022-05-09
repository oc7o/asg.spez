<template>
  <div>
    <section class="section is-medium" v-if="pageByCategoryAndSlug.category != null" v-html="content"></section>
  </div>
</template>
<script>
import gql from 'graphql-tag'

export default {
  apollo: {
    pageByCategoryAndSlug: {
      query: gql`
        query pageByCategoryAndSlug($category: String, $slug: String) {
            pageByCategoryAndSlug (category: $category, slug: $slug){
                title
                content
                category {
                    title
                }
            }
        }
      `,
      variables() {
        return {
          category: this.$route.params.slug1,
          slug: this.$route.params.slug2
        }
      },
    },
  },
  data () {
    return {}
  },
  computed: {
    content () {
      return this.$content(this.pageByCategoryAndSlug.content)
    }
  }
}
</script>