import { ref } from 'vue'
const getEducation = () => {
  const education = ref([])
  const error = ref(null)
  const backendUrl = import.meta.env.VITE_BACKEND_URL
  const load = async () => {
    try {
      const response = await fetch(`${backendUrl}/api/v1/educations`)
      if (!response.ok) {
        throw Error('No data available')
      }
      const data = await response.json()
      education.value = data
    } catch (error) {
      console.log('Something wrong!', error.message)
    }
  }
  return { education, error, load }
}

export default getEducation
