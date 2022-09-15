<template>
    <h2>Relatórios</h2>
    <div class="conteiner">
        <div class="row">
            <table class="table">
                <thead>
                    <th>Quantidade de pontos perdidos</th>
                    <td>{{relatorios.pontos_perdidos}}</td>
                </thead>

                <thead>
                    <th>Sobreviventes</th>
                    <th>Resultado</th>
                </thead>
                <tr>
                    <td>Porcentagem de infectados</td>
                    <td>{{relatorios.porcentagem_infectados}}%</td>
                    
                </tr>
                <tr>
                    <td>Porcentagem de não infectados</td>
                    <td>{{relatorios.porcentagem_nao_infectados}}%</td>
                </tr>
                <thead>
                    <th>Item</th>
                    <th>Média de itens/sobrevivente</th>
                </thead>
                <tr>
                    <td>Água</td>
                    <td>{{relatorios.media_aguas}}</td>
                </tr>
                <tr>
                    <td>Alimentação</td>
                    <td>{{relatorios.media_alimentacao}}</td>
                </tr>
                <tr>
                    <td>Medicação</td>
                    <td>{{relatorios.media_medicacao}}</td>
                </tr>
                <tr>
                    <td>Munição</td>
                    <td>{{relatorios.media_municao}}</td>
                </tr>
            </table>

        </div>

    </div>
</template>

<script>
    import axios from "axios";

    export default {
        name: "RelatorioView",
        data() {
            return {
            relatorios: [],

            };
        },
        mounted () {
            axios
            .get('http://localhost:8000/sobreviventes/relatorio/')
            .then(response => (this.relatorios = response.data))
            
        },

    };
    
</script>   