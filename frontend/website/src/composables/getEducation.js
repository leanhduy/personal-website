import { ref } from 'vue'
const getEducation = () => {
  const education = ref([])
  const error = ref(null)
  const load = async () => {
    try {
      const response = await fetch('http://localhost:3000/education')
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
