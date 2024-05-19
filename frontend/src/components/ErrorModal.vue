<script setup>
import { ref, watch } from 'vue';
import useEventsBus from '@/eventbus/eventBus.js';

const { bus } = useEventsBus();

const errorModalTriggerBtn = ref(null);
const errorMessage = ref(null);

watch(() => bus.value.get('errorEmit'), () => {
    errorMessage.value =  null;
    errorMessage.value = bus.value.get('errorEmit')[0];
    errorModalTriggerBtn.value.click();
})


</script>

<template>
    <!-- Button trigger modal -->
    <button ref="errorModalTriggerBtn" type="button" class="btn btn-primary" data-bs-toggle="modal" data-bs-target="#errorModal" hidden></button>

    <!-- Modal -->
    <div class="modal fade" id="errorModal" data-bs-backdrop="static" data-bs-keyboard="false" tabindex="-1" aria-labelledby="errorModalLabel" aria-hidden="true">
        <div class="modal-dialog modal-dialog-centered">
            <div class="modal-content">
                <div class="modal-header">
                    <h1 class="modal-title fs-5" id="errorModalLabel">Ooops, something went wrong...</h1>
                    <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                </div>
                <div class="modal-body">
                    <!-- Show simple error message if single string -->
                    <p v-if="typeof errorMessage === 'string'" class="card-text">{{ errorMessage }}</p>
                    <!-- Create unordered list for objects -->
                    <ul v-else-if="typeof errorMessage === 'object'">
                        <!-- Fill the list as it is for an array -->
                        <li v-if="Array.isArray(errorMessage)" v-for="(error, index) in errorMessage" :key="index">{{ error }}</li>
                        <!-- Fill create sublist for an object if needed or list "key: value" -->
                        <div v-else>
                           <li v-for="(value, key) in errorMessage" :key="key">{{ key }}:
                            <ul v-if="Array.isArray(value)">
                                <li v-for="(v, i) in value" :key="i">{{ v }}</li>
                            </ul>
                            <span v-else> {{ value }}</span>
                        </li>
                        </div>
                    </ul>
                </div>
            </div>
        </div>
    </div>
</template>

<style scoped>
.homepage-logo {
    width: 4rem;
    height: auto;
}
</style>
