import { ref } from 'vue'
const getProfile = () => {
  const profile = ref(null)
  const error = ref(null)
  const backendUrl = import.meta.env.VITE_BACKEND_URL
  const load = async () => {
    try {
      const response = await fetch(`${backendUrl}/api/v1/admin`)
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
