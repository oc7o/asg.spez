<template>
  <div>
    <section class="hero">
      <div class="hero-body">
        <p class="title">Albert-Schweitzer Gymnasium</p>
        <p class="subtitle">Spezialschulteil für ...</p>
        <div class="card">
          <div class="card-image">
            <figure class="image">
              <b-image :src="require('~/assets/img/hero.jpeg')"></b-image>
            </figure>
          </div>
        </div>
      </div>
    </section>
    <section class="section" v-for="page in last10EditedPages" :key="page.slug">
      <Card :page="page" />
    </section>
  </div>
</template>
<script>
import gql from 'graphql-tag'

export default {
  components: {
    // quillEditor
  },
  apollo: {
    last10EditedPages: gql`
      {
        last10EditedPages {
          title
          slug
          content
          updatedAt
          category {
            slug
          }
          author {
            firstName
            lastName
            username
          }
        }
      }
    `,
  },
  data() {
    return {}
  },
  computed: {
    
  },
}
</script>
<style scoped></style>
