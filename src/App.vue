<template>
  <div id="app">
    <img alt="Vue logo" src="./assets/logo.png">
    <CreateSobreviventes/>
    <br>
    <center>
      <GetSobreviventes/>
    </center>
    
  </div>
</template>

<script>
import GetSobreviventes from './components/GetSobreviventes.vue'
import CreateSobreviventes from './components/CreateSobreviventes.vue'


export default {
  name: 'App',
  components: {
    GetSobreviventes,
    CreateSobreviventes
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
