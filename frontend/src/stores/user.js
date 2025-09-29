import { ref } from 'vue'
import { defineStore } from 'pinia'
import {
  accessTokenApiCall,
  refreshTokenApiCall,
  verifyTokenApiCall,
  loginApiCall,
  logoutApiCall,
  logoutAllApiCall,
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

  // Auth Actions:

  /////////
  // JWT //
  /////////

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
      });
  }

  //////////
  // Knox //
  //////////

    async function login(username, password) {
        try {
            let response = await loginApiCall(username, password);
            accessToken.value = response.data.token;
            response = await userDataApiCall(accessToken.value);
            userData.value = response.data;
            return true;
        } catch (error) {
            emit('errorEmit', 'Provided credentials are not valid or can\'t be verified');
        }
    }

    async function logout() {
        try {
            await logoutApiCall(accessToken.value);
        } catch (error) {
            console.log('Token already expired');
        }
        accessToken.value = '';
        userData.value = {};
        emit('reloadEmit', true);
    }

    async function logoutAll() {
        try {
            await logoutAllApiCall(accessToken.value);
        } catch (error) {
            console.log('Token already expired');
        }
        accessToken.value = '';
        userData.value = {};
        emit('reloadEmit', true);
    }

    async function verifyTokenAndRefresh() {
        try {
            // Simply calling the backend with a refreshable token refreshes it:
            let response = await userDataApiCall(accessToken.value);
            userData.value = response.data;
        } catch (error) {
            // Max token lifetime expired:
            console.log('Max token lifetime expired');
            accessToken.value = '';
            userData.value = {};
            emit('reloadEmit', true);
        }
    }

  // General actions:

  async function passwordReset(new_pwd, conf_pwd) {
    if (!accessToken.value) {
      emit('errorEmit', 'You must login first');
      return false;
    }
    if (!new_pwd || !conf_pwd) {
      emit('errorEmit', 'Fill both password fields');
      return false;
    }
    if (new_pwd !== conf_pwd) {
      emit('errorEmit', 'The two password fields didn\'t match');
      return false;
    }
    return passwordResetApiCall(accessToken.value, new_pwd, conf_pwd)
      .then(() => true)
      .catch((error) => {
        emit('errorEmit', error.response.data);
        return false;
      })
  }

  function isAuthenticated() {
    return !(!accessToken.value);
  }

  function isAdmin() {
    if (!isAuthenticated()) return false;
    return userData.value.is_superuser || userData.value.is_staff;
  }

  return { accessToken, refreshToken, userData, login, logout, passwordReset, verifyTokenAndRefresh, isAuthenticated, isAdmin }
},
{
  persist: {
    storage: localStorage,
    paths: ['accessToken', 'refreshToken', 'userData'],
  }
})
