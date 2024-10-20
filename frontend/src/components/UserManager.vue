<script setup>
import { ref, computed, onBeforeMount } from 'vue';
import { useUserStore } from '@/stores/user.js';

const user = useUserStore();

const buttonsDisabler = ref(false);

// Login states:
const username = ref(null);
const password = ref(null);
const loginModalTriggerBtn = ref(null);
const loginModalCloseBtn = ref(null);

// Pswd Change states:
const newPswd = ref(null);
const confPswd = ref(null);
const changePswdModalTriggerBtn = ref(null);
const changePswdModalCloseBtn = ref(null);

const connected = computed(() => user.accessToken !== '');

onBeforeMount(async() => {
    if (user.accessToken) {
        await user.verifyTokenAndRefresh();
    }
});

async function userLogin() {
    loginModalCloseBtn.value.click();
    await user.login(username.value, password.value);
    if (user.userData.password_must_be_reset) {
        changePswdModalTriggerBtn.value.click();
    }
}

async function userChangePswd() {
    changePswdModalCloseBtn.value.click();
    await user.passwordReset(newPswd.value, confPswd.value);
}
</script>

<template>
    <div v-if="connected" class="d-flex">
        <div class="card text-center text-bg-dark connector">
            <div class="card-body content-wrapper pt-2">
                <img class="user-logo me-2" src="@/assets/user-light.svg" alt="user icon">
                <p class="card-text">{{ user.userData.username }}</p>
            </div>
        </div>
        <button @click="user.logout()" class="btn btn-dark connector ms-1">Logout</button>
    </div>

    <!-- Login modal trigger -->
    <button v-else ref="loginModalTriggerBtn"
                   :disabled="buttonsDisabler"
                   class="btn btn-dark connector"
                   data-bs-toggle="modal"
                   data-bs-target="#loginModal">Login</button>
    <!-- Login modal -->
    <div class="modal fade" id="loginModal" data-bs-backdrop="static" data-bs-keyboard="false" tabindex="-1" aria-labelledby="loginModalLabel" aria-hidden="true">
        <div class="modal-dialog modal-dialog-centered">
            <div class="modal-content">
                <div class="modal-header">
                    <h1 class="modal-title fs-5" id="loginModalLabel">Insert your credentials</h1>
                    <button ref="loginModalCloseBtn" type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                </div>
                <div class="modal-body">
                    <!-- Login Form -->
                    <form @submit.prevent="userLogin">
                        <div class="mb-3">
                            <label for="usernameEmailInput" class="form-label">Username/Email</label>
                            <input v-model="username" type="text" class="form-control" id="usernameEmailInput">
                        </div>
                        <div class="mb-3">
                            <label for="passwordInput" class="form-label">Password</label>
                            <input v-model="password" type="password" class="form-control" id="passwordInput">
                        </div>
                        <button id="loginBtn" type="submit" class="btn btn-primary blue-btn">Login</button>
                    </form>
                </div>
            </div>
        </div>
    </div>

    <!-- Pswd Change modal trigger -->
    <button ref="changePswdModalTriggerBtn" type="button" class="btn btn-primary" data-bs-toggle="modal" data-bs-target="#changePswdModal" hidden></button>
    <!-- Pswd Change modal -->
    <div class="modal fade" id="changePswdModal" data-bs-backdrop="static" data-bs-keyboard="false" tabindex="-1" aria-labelledby="changePswdModalLabel" aria-hidden="true">
        <div class="modal-dialog modal-dialog-centered">
            <div class="modal-content">
                <div class="modal-header">
                    <h1 class="modal-title fs-5" id="changePswdModalLabel">Insert a new password for your account</h1>
                    <button ref="changePswdModalCloseBtn" type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                </div>
                <div class="modal-body">
                    <!-- Pswd Reset Form -->
                    <form @submit.prevent="userChangePswd">
                        <div class="mb-3">
                            <label for="newPswdInput" class="form-label">New Password</label>
                            <input v-model="newPswd" type="password" class="form-control" id="newPswdInput">
                        </div>
                        <div class="mb-3">
                            <label for="confPswdInput" class="form-label">Confirm Password</label>
                            <input v-model="confPswd" type="password" class="form-control" id="confPswdInput">
                        </div>
                        <button id="changePswdBtn" type="submit" class="btn btn-primary blue-btn">Update Password</button>
                    </form>
                </div>
            </div>
        </div>
    </div>
</template>

<style scoped>
.connector {
    height: 2.6rem;
}
</style>
