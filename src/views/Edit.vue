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
              <tr>
                <td>{{ sobreviventes.nome_sobrevivente }}</td>
                <td>{{ sobreviventes.idade_sobrevivente }}</td>
                <td>{{ sobreviventes.sexo_sobrevivente }}</td>
                <td>{{ sobreviventes.latitude_sobrevivente }}</td>
                <td>{{ sobreviventes.longitude_sobrevivente }}</td>
                <td>{{ sobreviventes.infectato }}</td>
                <td><button class="btn btn-info">editar</button></td>
              </tr>
            
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
        .get('http://127.0.0.1:8000/sobreviventes/sobrevivente/'+this.$route.params.id+'/')
        .then(response => (this.sobreviventes = response.data))
       
    },
  
  };

  </script>