<template>

  <div>
  <table class="table table-striped mt-4">
      <thead>
      <tr>
        <th scope="col">Fecha de Nacimiento</th>
        <th scope="col">nombre autor</th>
        <th scope="col">nombre de libro</th>
      </tr>
      </thead>
      <tbody>
      <tr v-for="input in directory.edges" :key="input.id">
        <td>{{ input.node.allAutores.FechaNacimiento }}</td>
        <td>{{ input.node.allAutores.name }}</td>
        <td>{{ input.node.allAutores.category.name }}</td>
      </tr>
      </tbody>
    </table>
  </div>

</template>

<script>
  import axios from 'axios'
  export default{
        name: 'libros',
    data(){
      return {
      	directory: []
      }
    },
  methods:{
  async mounted () {
     try {
       var result = await axios({
         method: 'POST',
         url: 'http://127.0.0.1:8000/graphql',
         data: {
            query: `
            {
              allAutores {
              edges {
                node {
                    id,
                    name,
                    FechaNacimiento,
                category {
                    id,
                    name,
                    Descripcion,
               }
             }
           }
         }
           `
         }
       })
       this.directory = result.data.data.allAutores
     } catch (error) {
       console.error(error)
     }
   } }
 }
</script>

<style scoped>
</style>
