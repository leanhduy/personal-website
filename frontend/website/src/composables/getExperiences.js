import { ref } from 'vue'
const getExperiences = () => {
  const experiences = ref([])
  const error = ref(null)
  const load = async () => {
    try {
      const response = await fetch('http://localhost:8000/api/v1/experiences')
      if (!response.ok) {
        throw Error('No data available')
      }
      const data = await response.json()
      experiences.value = data
      // sort the experiences based on start date (latest comes first)
      experiences.value.sort((a, b) => {
        return new Date(b.start_date) - new Date(a.start_date)
      })
    } catch (error) {
      console.log('Something wrong!', error.message)
    }
  }
  return { experiences, error, load }
}

export default getExperiences
