<template>
    <section>
      <div>
        <form class="input-feild" @submit.prevent="handleSubmit">
          <input
            class="search-input"
            type="text"
            placeholder="Nome"
            v-model="nome_sobrevivente"
          />
          <input
            class="search-input"
            type="text"
            placeholder="Idade"
            v-model="idade_sobrevivente"
          />
          <input
            class="search-input"
            type="text"
            placeholder="Sexo"
            v-model="sexo_sobrevivente"
          />
          <input
            class="search-input"
            type="text"
            placeholder="latitude"
            v-model="latitude_sobrevivente"
          />
          <input
            class="search-input"
            type="text"
            placeholder="Longitude"
            v-model="longitude_sobrevivente"
          />
          <button class="btn-search">Adicionar sobrevivente</button>
        </form>

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
          nome_sobrevivente: "",
          idade_sobrevivente: "",
          sexo_sobrevivente: "",
          latitude_sobrevivente: "",
          longitude_sobrevivente: "",
        };
      },
      methods: {
        handleSubmit() {
          axios
            .post("http://localhost:8000/sobreviventes/adicionarsobrevivente/", {
              nome_sobrevivente: this.nome_sobrevivente,
              idade_sobrevivente: this.idade_sobrevivente,
              sexo_sobrevivente: this.sexo_sobrevivente,
              latitude_sobrevivente: this.latitude_sobrevivente,
              longitude_sobrevivente: this.latitude_sobrevivente,
              flags_infectado: 0,
              infectato: false,
              itens:[{
                inventario_id: "1",
                qtd: "2"
              }]
            })
            .then((response) => {
              const data = response.data;
              this.sobreviventes.push(data);
              this.nome_sobrevivente = "";
              this.idade_sobrevivente = "";
              this.sexo_sobrevivente = "";
              this.latitude_sobrevivente = "";
              this.longitude_sobrevivente = "";

            });
        },
      },
    };
    </script>