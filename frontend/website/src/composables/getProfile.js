import { ref } from 'vue'
const getProfile = () => {
  const profile = ref(null)
  const error = ref(null)
  const load = async () => {
    try {
      const response = await fetch('http://localhost:3000/profile')
      if (!response.ok) {
        throw Error('No data available')
      }
      const data = await response.json()
      profile.value = data
    } catch (error) {
      console.log('Something wrong!', error.message)
    }
  }
  return { profile, error, load }
}

export default getProfile
