import { ref } from 'vue'
const getSkills = () => {
  const skills = ref([])
  const error = ref(null)
  const load = async () => {
    try {
      const response = await fetch('http://localhost:8000/api/v1/skills')
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
