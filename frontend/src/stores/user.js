import { ref } from 'vue'
import { defineStore } from 'pinia'
import {
  accessTokenApiCall,
  refreshTokenApiCall,
  verifyTokenApiCall,
  userDataApiCall,
  passwordResetApiCall,
} from '@/helpers/api-calls.js'
import useEventsBus from '@/eventbus/eventBus.js'
const { emit } = useEventsBus()


export const useUserStore = defineStore('user', () => {
  // Stotes:
  const accessToken = ref('')
  const refreshToken = ref('')
  const userData = ref({})

  // Actions:
  async function login(username, password) {
    try {
      let response = await accessTokenApiCall(username, password);
      accessToken.value = response.data.access;
      refreshToken.value = response.data.refresh;
      response = await userDataApiCall(accessToken.value);
      userData.value = response.data;
    } catch (error) {
      emit('errorEmit', 'Provided credentials are not valid or can\'t be verified');
    }
  }

  async function logout() {
    accessToken.value = '';
    refreshToken.value = '';
    userData.value = {};
    emit('reloadEmit', true);
  }

  async function passwordReset(new_pwd, conf_pwd) {
    if (new_pwd !== conf_pwd) {
      emit('errorEmit', 'The two password fields didn\'t match');
      return false;
    }
    if (!accessToken.value) {
      emit('errorEmit', 'You must login first');
      return false;
    }
    passwordResetApiCall(accessToken.value, new_pwd, conf_pwd)
      .then(() => true)
      .catch((error) => {
        emit('errorEmit', error.response.data);
        return false;
      })
  }

  async function verifyTokenAndRefresh() {
    verifyTokenApiCall(accessToken.value)
      .catch(async () => {
        try {
          const response = await refreshTokenApiCall(refreshToken.value);
          accessToken.value = response.data.access;
          refreshToken.value = response.data.refresh;
          response = await userDataApiCall(accessToken.value);
          userData.value = response.data;
        } catch (error) {
          console.log(error);
          accessToken.value = '';
          refreshToken.value = '';
          userData.value = {};
        }
      })
  }

  return { accessToken, refreshToken, userData, login, logout, passwordReset, verifyTokenAndRefresh }
},
{
  persist: {
    storage: localStorage,
    paths: ['accessToken', 'refreshToken', 'userData'],
  }
})
