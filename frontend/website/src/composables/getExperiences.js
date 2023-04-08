import { ref } from 'vue'
const getExperiences = () => {
  const experiences = ref([])
  const error = ref(null)
  const load = async () => {
    try {
      const response = await fetch('http://localhost:3000/experiences')
      if (!response.ok) {
        throw Error('No data available')
      }
      const data = await response.json()
      experiences.value = data
    } catch (error) {
      console.log('Something wrong!', error.message)
    }
  }
  return { experiences, error, load }
}

export default getExperiences
