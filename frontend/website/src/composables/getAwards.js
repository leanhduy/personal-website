import { ref } from 'vue'
const getAwards = () => {
  const awards = ref([])
  const error = ref(null)
  const backendUrl = process.env.BACKEND_URL
  const load = async () => {
    try {
      const response = await fetch(`${backendUrl}/api/v1/awards`)
      if (!response.ok) {
        throw Error('No data available')
      }
      const data = await response.json()
      awards.value = data
      // Sort the awards by date taken (Latest come first)
      data.sort((award1, award2) => {
        if (award1.date_taken > award2.date_taken) {
          return -1
        } else if (award1.date_taken < award2.date_taken) {
          return 1
        } else {
          return 0
        }
      })
    } catch (error) {
      console.log('Something wrong!', error.message)
    }
  }
  return { awards, error, load }
}

export default getAwards
