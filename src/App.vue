<template>
   <div class="conteiner"> 
    <nav>
      <router-link to="/">Home</router-link> |
      <router-link to="/register">Registrar</router-link> |
      
    </nav>
    <div class="conteudo">
      <router-view/>
    </div>
    
  </div>
  
</template>

<style>

  .conteiner{
    min-height: 100vh;
    height: 100%;
    background-color: white;
    margin: auto;
    width:60%;
    padding: 10px;
  }

  #app {
    height: 100%;
    background-color: #2c3e50;
    font-family: Avenir, Helvetica, Arial, sans-serif;
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
    text-align: center;
    color: #2c3e50;
  }

  nav {
    padding: 30px;
  }

  nav a {
    font-weight: bold;
    color: #2c3e50;
  }

  nav a.router-link-exact-active {
    color: #42b983;
  }
</style>
