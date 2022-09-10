<template>
  <div id="app">
    <img alt="Vue logo" src="./assets/logo.png">
    <GetPage/>
  </div>
</template>

<script>
import GetPage from './components/GetPage.vue'

export default {
  name: 'App',
  components: {
    GetPage
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
