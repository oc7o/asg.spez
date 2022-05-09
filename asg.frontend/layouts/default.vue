<template>
  <div id="background">
    <Navbar />
    <br>
    <div class="container card">
      <Nuxt id="content" />
    </div>
    <br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br>
    <Footer />
  </div>
</template>

<script>
export default {
  name: 'DefaultLayout',
}
</script>

<style scoped>
#background {
  background-image: url("https://external-content.duckduckgo.com/iu/?u=http%3A%2F%2Fandy-wall.de%2Fmedia%2Fimage%2F06%2Fc3%2Faa%2FLines_Bow_600x600%402x.png&f=1&nofb=1");
  font-family: 'Oleo Script Swash Caps', cursive;
}

.card {
  background-color: rgba(255, 255, 255, 0.85)
}
</style>