<template>
  <nuxt-link :to="uri">
    <div class="card">
      <!-- <div class="card-image">
      <figure class="image is-4by3">
        <img
          src="https://bulma.io/images/placeholders/1280x960.png"
          alt="Placeholder image"
        />
      </figure>
    </div> -->
      <div class="card-content">
        <div class="media">
          <div class="media-left">
            <figure class="image is-48x48">
              <img
                src="https://bulma.io/images/placeholders/96x96.png"
                alt="Placeholder image"
              />
            </figure>
          </div>
          <div class="media-content">
            <p class="title is-4">{{ page.title }}</p>
            <p class="subtitle is-6">
              {{ page.author.firstName }} {{ page.author.lastName }} aka. @{{
                page.author.username
              }}
            </p>
          </div>
        </div>
        <div class="content">
          {{ w100 }}
          <br />
          <time datetime="2016-1-1">{{ page.updatedAt }}</time>
        </div>
      </div>
    </div>
  </nuxt-link>
</template>
<script>
export default {
  props: ['page'],
  computed: {
    content() {
      return this.$content(this.page.content)
    },
    w100() {
      const html = this.$content(this.page.content)
      if (html.includes('<p>') && html.includes('</p>')) {
        const start = html.indexOf('<p>')
        const end = html.indexOf('</p>')
        var result = html.slice(start + 3, end)
        if (result.lenth > 100) {
          result = result.slice(0, 100) + '...'
        } else {
          return result
        }
      } else {
        return ''
      }
    },
    uri() {
      if (this.page.category != null) {
        return `/${this.page.category.slug}/${this.page.slug}`
      } else {
        return `/${this.page.slug}`
      }
    },
  },
}
</script>
