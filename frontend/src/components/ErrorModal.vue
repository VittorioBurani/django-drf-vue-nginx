<script setup>
import { ref, watch } from 'vue';
import useEventsBus from '@/eventbus/eventBus.js';

const { bus } = useEventsBus();

const errorModalTriggerBtn = ref(null);
const errorMessage = ref('');

watch(() => bus.value.get('errorEmit'), () => {
    errorMessage.value = '';
    errorModalTriggerBtn.value.click();
    for (let [key, value] of Object.entries(bus.value.get('errorEmit'))) {
        errorMessage.value += value;
    }
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
                    <p class="card-text">{{ errorMessage }}</p>
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
