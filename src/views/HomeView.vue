<template>
  <section>
      <h2>Sobreviventes</h2>
      <div class="conteiner">
        <div class="row col-md-6 center">

        
          <table class="table ">
            <thead >
              <tr>
                <th scope="col">Name</th>
                <th scope="col">Idade</th>
                <th scope="col">Sexo</th>
                <th scope="col">Latitude</th>
                <th scope="col">Longitude</th>
                <th scope="col">Infectado</th>
                <th>-</th>
              </tr>
            </thead>
            <tbody v-for="(sobrevivente, index) in sobreviventes" :key="index">
              <tr>
                <td>{{ sobrevivente.nome_sobrevivente }}</td>
                <td>{{ sobrevivente.idade_sobrevivente }}</td>
                <td>{{ sobrevivente.sexo_sobrevivente }}</td>
                <td>{{ sobrevivente.latitude_sobrevivente }}</td>
                <td>{{ sobrevivente.longitude_sobrevivente }}</td>
                <td>{{ sobrevivente.infectato }}</td>
                <td><button class="btn btn-info">editar</button></td>
              </tr>
            </tbody>
          </table>
        </div>
      </div>
  </section>

</template>

<script>
  import axios from "axios";

  export default {

    name: "CreateSobreviventes",
    data() {
      return {
        sobreviventes: [],
        

      };
    },
    mounted () {
      axios
        .get('http://localhost:8000/sobreviventes/')
        .then(response => (this.sobreviventes = response.data))
        
    },
  
  };


  
  </script>