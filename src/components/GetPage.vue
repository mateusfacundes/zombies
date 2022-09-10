<template>

<section>
<div class="conteiner">
  <div class="row col-md-6 center">

  
    <table class="table">
      <thead >
        <tr>
          <th scope="col">#</th>
          <th scope="col">Name</th>
          <th scope="col">Idade</th>
          <th scope="col">Sexo</th>
          <th scope="col">Latitude</th>
          <th scope="col">Longitude</th>
          <th scope="col">Infectado</th>
        </tr>
      </thead>
      <tbody v-for="(sobrevivente, index) in sobreviventes" :key="index">
        <tr>
          <th scope="row">{{ sobrevivente.sobreviventes_id }}</th>
          <td>{{ sobrevivente.nome_sobrevivente }}</td>
          <td>{{ sobrevivente.idade_sobrevivente }}</td>
          <td>{{ sobrevivente.sexo_sobrevivente }}</td>
          <td>{{ sobrevivente.latitude_sobrevivente }}</td>
          <td>{{ sobrevivente.longitude_sobrevivente }}</td>
          <td>{{ sobrevivente.infectato }}</td>
        </tr>
      </tbody>
    </table>
  </div>
</div>
</section>

</template>

<script>
  import axios from 'axios';
  
  export default {

    name: "GetPage",
  
    data() {
      return {
        sobreviventes: [],
      };
    },

    mounted () {
    axios
      .get('http://localhost:8000/sobreviventes/')
      .then(response => (this.sobreviventes = response.data))
  }

    
  }

    </script>