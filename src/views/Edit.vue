<template>
  <section>
      <h2>Sobrevivente</h2>
      <div class="conteiner register">
        <div class="row col-md-6 ">

          <form   @submit.prevent="enviar">
            <table class="table ">
              <thead >
                <tr>
                  <th scope="col">Name</th>
                  <th scope="col">Idade</th>
                  <th scope="col">Sexo</th>
                  <th scope="col">Latitude</th>
                  <th scope="col">Longitude</th>
                  <th scope="col">Infectado</th>
                </tr>
              </thead>
              <thead >
                <tr>
                  <td>{{ sobreviventes.nome_sobrevivente }}</td>
                  <td>{{ sobreviventes.idade_sobrevivente }}</td>
                  <td>{{ sobreviventes.sexo_sobrevivente }}</td>
                  
                  <td><input class="loc" type="number" :placeholder="sobreviventes.latitude_sobrevivente" v-model="novalatitude"></td>
                  <td><input class="loc" type="number" :placeholder="sobreviventes.longitude_sobrevivente" v-model="novalongitude"></td>
                  
                  <td>{{ sobreviventes.infectato }}</td>
                </tr>
              </thead>
            </table>
            
            <table class="table">
              <thead >
                <tr>
                  <th scope="col">Item</th>
                  <th scope="col">Quantidade</th>              
                </tr>
              </thead>
                <tbody v-for="(item, index) in inventario" :key="index">
                  <tr>
                    <td>{{ item.item.nome_item }}</td>
                    <td>{{ item.qtd }}</td>
                  </tr>
                </tbody>
            </table>
            
            <button class="btn-search btn btn-outline-success">Atualizar coordenadas</button>
          </form>
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
        inventario: [],
        novalatitude: '',
        novalongitude: '',
      };
    },
    methods:{
      enviar(){
        console.log(this.novalatitude);
        this.sobreviventes.latitude_sobrevivente = this.novalatitude;
        this.sobreviventes.longitude_sobrevivente = this.novalongitude;
        axios
          .put('http://127.0.0.1:8000/sobreviventes/atualizarsobrevivente/'+this.$route.params.id+'/', this.sobreviventes)
          .then(response => (window.alert(response.data)))

      }
    },
    mounted () {
      
      axios
        .get('http://127.0.0.1:8000/sobreviventes/sobrevivente/'+this.$route.params.id+'/')
        .then(response => (this.sobreviventes = response.data))
      axios
        .get('http://127.0.0.1:8000/sobreviventes/sobreviventesitens/'+this.$route.params.id+'/')
        .then(response => (this.inventario = response.data))
    },
  
  };

  </script>

  <style>
    .register{
      height: 900px;
    }
    .loc{
      width: 100px;
    }
  </style>