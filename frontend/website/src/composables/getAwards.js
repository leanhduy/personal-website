import { ref } from 'vue'
const getAwards = () => {
  const awards = ref([])
  const error = ref(null)
  const load = async () => {
    try {
      const response = await fetch('http://localhost:3000/awards')
      if (!response.ok) {
        throw Error('No data available')
      }
      const data = await response.json()
      awards.value = data
    } catch (error) {
      console.log('Something wrong!', error.message)
    }
  }
  return { awards, error, load }
}

export default getAwards
