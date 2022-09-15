<template>
  <section>
      <h2>Sobrevivente</h2>
      <div class="conteiner register">
        <div class="row col-md-6 ">

          <form   @submit.prevent="update">
            <table class="table ">
              <thead >
                <tr>
                  <th scope="col">Name</th>
                  <th scope="col">Idade</th>
                  <th scope="col">Sexo</th>
                  <th scope="col">Latitude</th>
                  <th scope="col">Longitude</th>
                  <th scope="col">Infectado</th>
                  <th scope="col">Alertas</th>
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
                  <td>{{ sobreviventes.flags_infectado }}</td>
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
            
            <button class=" btn btn-outline-success">Atualizar coordenadas</button>

            
          </form>
          <button id="flag" @click="flaging" class="botao btn btn-outline-danger">Acusar infecção</button>
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

      };
    },
    methods:{
      update(){
        this.sobreviventes.latitude_sobrevivente = this.novalatitude;
        this.sobreviventes.longitude_sobrevivente = this.novalongitude;
        axios
          .put('http://127.0.0.1:8000/sobreviventes/atualizarsobrevivente/'+this.$route.params.id+'/', this.sobreviventes)
          .then(response => (window.alert(response.data)))

      },
      flaging(){
        
        if (this.sobreviventes.flags_infectado >=3){
          this.sobreviventes.infectato = true;
        }
        else{
          this.sobreviventes.flags_infectado += 1;
        }
        axios
          .put('http://127.0.0.1:8000/sobreviventes/atualizarsobrevivente/'+this.$route.params.id+'/', this.sobreviventes)
          .then(response => (window.alert('+ 1 flag para este sobrevivente'), response))
        
      }
    },
    mounted () {

      axios
        .get('http://127.0.0.1:8000/sobreviventes/sobrevivente/'+this.$route.params.id+'/')
        .then(response => (this.sobreviventes = response.data))
        .then(response => {
          console.log(response.data)
          if (this.sobreviventes.infectato == true){
            var bnt = document.getElementById("flag");
            bnt.outerHTML = "";
          }
        })
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
    .botao{
      margin: auto;
      width:60%;
      padding: 10px;
    }
  </style>