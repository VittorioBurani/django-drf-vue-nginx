<script setup>
import { ref } from 'vue';

const props = defineProps({
    'items': Array,
    'multiple': Boolean,
    'key2show': {
        type: String,
        default: "name"
    },
})

const singleValue = ref(null);
const values = ref([]);

function updateValue() {
    if (!props.multiple) {
        return singleValue.value.value;
    } else {
        if (values.value.includes(singleValue.value.value)) {
            values.value = values.value.filter((value) => value !== singleValue.value.value);
        } else {
            values.value = [...values.value, singleValue.value.value];
        }
        return values.value;
    }
}
</script>

<template>
    <select @change="$emit('changed', updateValue())" ref="singleValue" class="form-select" aria-label="Default select example" :multiple="props.multiple">
        <option selected>---</option>
        <option v-for="item in props.items" :key="item.id" :value="item.id">{{ item[props.key2show] }}</option>
    </select>
</template>
