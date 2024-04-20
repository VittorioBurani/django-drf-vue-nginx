const BACKEND_URL = import.meta.env.VITE_BACKEND_URL

const BACKEND_API_URL = `${BACKEND_URL}/api`
const BACKEND_API_AUTH_URL = `${BACKEND_API_URL}/auth`

export default {
    BACKEND_API_URL,
    BACKEND_API_AUTH_URL,
}
