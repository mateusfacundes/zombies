<template>
   <section>
    
      <h2>Adicionar Sobrevivente</h2>
      <div class="conteiner">
        <div class="row col-md-12 center">
            <form  @submit.prevent="handleSubmit">
              <div class="row">
                <div class="form-group " >
                      <input
                      type="text"
                      placeholder="Nome"
                      v-model="nome_sobrevivente"
                      />
                </div>
                <div class="form-group">
                    <input
                      
                      type="text"
                      placeholder="Idade"
                      v-model="idade_sobrevivente"
                    />
                </div>
                <div class="form-group" >
                  <select   class="form-control form-control-sm" v-model="sexo_sobrevivente">
                        <option value="">Sexo</option>
                        <option value="Masculino">Masculino</option>
                        <option value="feminino">feminino</option>
                  </select>
                </div>
                <div class="form-group " >
                  <input
                    type="text"
                    placeholder="latitude"
                    v-model="latitude_sobrevivente"
                  />
                </div>
                <div class="form-group ">
                  <input
                    type="text"
                    placeholder="Longitude"
                    v-model="longitude_sobrevivente"
                  />
                </div>
              </div>
              <button @click="tamanhoBotao" class="btn btn" type="button">+ Itens</button>
              <button @click="input--" class="btn btn" type="button" >- Itens</button>

              <div v-for="i in input" v-bind:key="i" class="row">
                <div class="form-group " >
                  <select :id="'seletor'+i" class="form-control form-control-sm" >
                    <option value="">Escolha um item</option>
                    <option v-for="item in itensmostrar" :value="item.inventario_id" v-bind:key="item">{{ item.nome_item }}</option>
                  </select>
                </div>
                <div class="form-group">
                  <input :id="'qtd'+i"
                    type="text"
                    placeholder="Quantidade"
                    
                  />
                </div>
              </div>
              <div class="form-group row">
                <button class="btn-search">Adicionar sobrevivente</button>
              </div>
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
        itensmostrar: [],
        nome_sobrevivente: "",
        idade_sobrevivente: "",
        sexo_sobrevivente: "",
        latitude_sobrevivente: "",
        longitude_sobrevivente: "",
        inventario_id:"",
        qtd:[],
        input: 1,
        itens: []

      };
    },
    methods: {
      tamanhoBotao(){
        if (this.input < 4){
          this.input++;
        }
      },
      handleSubmit() {
        var i = 1;
        while( i<= this.input){
          var option = document.getElementById("seletor"+i);
          var qtdopt = document.getElementById("qtd"+i);
          
          this.itens.push({
            inventario_id: option.value,
            qtd: qtdopt.value
          });

          console.log(this.itens);
          i++;
        }
        
        axios
          .post("http://localhost:8000/sobreviventes/adicionarsobrevivente/", {
            nome_sobrevivente: this.nome_sobrevivente,
            idade_sobrevivente: this.idade_sobrevivente,
            sexo_sobrevivente: this.sexo_sobrevivente,
            latitude_sobrevivente: this.latitude_sobrevivente,
            longitude_sobrevivente: this.latitude_sobrevivente,
            flags_infectado: 0,
            infectato: false,
            itens: this.itens
          })
          .then((response) => {
              const data = response.data;
              window.alert(data);
              this.nome_sobrevivente = "";
              this.idade_sobrevivente = "";
              this.sexo_sobrevivente = "";
              this.latitude_sobrevivente = "";
              this.longitude_sobrevivente = "";
              this.input = 1;

            });

      
      },
    },
    mounted () {
      axios
        .get('http://127.0.0.1:8000/sobreviventes/itens')
        .then(response => (this.itensmostrar = response.data))
        console.log(this.itensmostrar)
    },
    components: {
      
    },

  };


  
</script>
