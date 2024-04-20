<script setup>
import { watch } from 'vue'
import { RouterView } from 'vue-router'
import Navbar from '@/components/Navbar.vue'
import ErrorModal from '@/components/ErrorModal.vue';
import useEventsBus from '@/eventbus/eventBus.js';

const { bus } = useEventsBus();

watch(() => bus.value.get('reloadEmit'), () => {
  bus.value.set('reloadEmit', false);
  window.location.reload();
})
</script>

<template>
  <div class="vstack gap-4">
    <Navbar />
    <div class="container mx-0 px-0">
      <RouterView/>
      <ErrorModal />
    </div>
  </div>
</template>
