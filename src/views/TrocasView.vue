<template>
    <h2>Trocas</h2>
    <div class="conteiner">
        <div class="row">
            <h3>Escolha os sobreviventes que irão negociar</h3>
            <div class="row">
                <div class="form-group " >
                    <select :id="'seletor'+i" class="form-control form-control-sm" >
                    <option value="">Escolha o primeiro sobrevivente</option>
                    <option v-for="sobrevivente in sobreviventes1" :value="sobrevivente.id_sobrevivente" v-bind:key="sobrevivente">{{ sobrevivente.nome_sobrevivente }}</option>
                    </select>
                </div>
                <h3>x</h3>
                <div class="form-group " >
                    <select :id="'seletor'+i" class="form-control form-control-sm" >
                    <option value="">Escolha o primeiro sobrevivente</option>
                    <option v-for="sobrevivente in sobreviventes2" :value="sobrevivente.id_sobrevivente" v-bind:key="sobrevivente">{{ sobrevivente.nome_sobrevivente }}</option>
                    </select>
                </div>
            </div>
      </div>
    </div>

</template>

<script>
    import axios from "axios";

    export default {

        name: "TrocasView",
        data() {
            return {
            sobreviventes1: [],
            sobreviventes2: [],
            
            };
        },
        mounted () {
            axios
            .get('http://localhost:8000/sobreviventes/')
            .then(response => (this.sobreviventes1 = response.data, this.sobreviventes2 = response.data))
            
        },

    };
</script>