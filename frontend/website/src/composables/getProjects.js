import { ref } from 'vue'
const getProjects = () => {
  const projects = ref([])
  const error = ref(null)
  const load = async () => {
    try {
      // const response = await fetch('http://localhost:3000/projects')
      const response = await fetch('http://localhost:8000/api/v1/projects')
      if (!response.ok) {
        throw Error('No data available')
      }
      const data = await response.json()
      projects.value = data
    } catch (error) {
      console.log('Something wrong!', error.message)
    }
  }
  return { projects, error, load }
}

export default getProjects
