import { ref } from 'vue'
const getSkills = () => {
  const skills = ref([])
  const error = ref(null)
  const backendUrl = process.env.VITE_BACKEND_URL
  const load = async () => {
    try {
      const response = await fetch(`${backendUrl}/api/v1/skills`)
      if (!response.ok) {
        throw Error('No data available')
      }
      const data = await response.json()
      skills.value = data
    } catch (error) {
      console.log('Something wrong!', error.message)
    }
  }
  return { skills, error, load }
}

export default getSkills
