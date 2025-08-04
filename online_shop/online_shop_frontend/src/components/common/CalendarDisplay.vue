<template>
  <div class="calendar">
    <div class="calendar-header">
      <button @click="prevMonth">＜</button>
      <span>{{ currentYear }}年{{ currentMonth + 1 }}月</span>
      <button @click="nextMonth">＞</button>
    </div>
    <div class="calendar-grid">
      <div class="day-header" v-for="(d, i) in dayNames" :key="i">{{ d }}</div>
      <div
        v-for="(date, index) in calendarDates"
        :key="index"
        class="calendar-day"
        :class="{
          // saturday: date.getDay() === 6 && isCurrentMonth(date),
          sunday: date.getDay() === 2 && isCurrentMonth(date),
          holiday: isHoliday(date) && isCurrentMonth(date),
          today: isToday(date) && isCurrentMonth(date)
        }"
      >
        <span v-if="isCurrentMonth(date)">{{ date.getDate() }}</span>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, computed, onMounted } from 'vue'
import axios from 'axios'

// 获取祝日API
const getHolidaysAPI = () => {
  return axios.get('https://holidays-jp.github.io/api/v1/date.json')
}

const today = new Date()
const currentYear = ref(today.getFullYear())
const currentMonth = ref(today.getMonth())
const holidays = ref({})

// 星期标题
const dayNames = ['日', '月', '火', '水', '木', '金', '土']

// 判断是否是今天
const isToday = (date) => {
  const d = new Date()
  return (
    date.getFullYear() === d.getFullYear() &&
    date.getMonth() === d.getMonth() &&
    date.getDate() === d.getDate()
  )
}

// 判断是否为当月日期
const isCurrentMonth = (date) => {
  return (
    date.getFullYear() === currentYear.value &&
    date.getMonth() === currentMonth.value
  )
}

// 判断是否是祝日
const isHoliday = (date) => {
  const dateStr = date.toISOString().split('T')[0]
  return holidays.value[dateStr] !== undefined
}

// 生成当前月的日历格子
const calendarDates = computed(() => {
  const year = currentYear.value
  const month = currentMonth.value
  const firstDay = new Date(year, month, 1)
  const lastDay = new Date(year, month + 1, 0)

  const startDate = new Date(firstDay)
  startDate.setDate(startDate.getDate() - firstDay.getDay())

  const endDate = new Date(lastDay)
  endDate.setDate(endDate.getDate() + (6 - lastDay.getDay()))

  const dates = []
  for (let d = new Date(startDate); d <= endDate; d.setDate(d.getDate() + 1)) {
    dates.push(new Date(d))
  }
  return dates
})

// 上一个月
const prevMonth = () => {
  if (currentMonth.value === 0) {
    currentMonth.value = 11
    currentYear.value--
  } else {
    currentMonth.value--
  }
}

// 下一个月
const nextMonth = () => {
  if (currentMonth.value === 11) {
    currentMonth.value = 0
    currentYear.value++
  } else {
    currentMonth.value++
  }
}

// 加载祝日
onMounted(async () => {
  const res = await getHolidaysAPI()
  holidays.value = res.data
})
</script>

<style scoped>
.calendar {
  width: 100%;
  font-family: sans-serif;
}
.calendar-header {
  display: flex;
  justify-content: center;
  align-items: center;
  gap: 20px;
  margin-bottom: 10px;
}
.calendar-grid {
  display: grid;
  grid-template-columns: repeat(7, 1fr);
}
.day-header {
  font-weight: bold;
  text-align: center;
  padding: 5px;
}
.calendar-day {
  height: 40px;
  text-align: center;
  line-height: 40px;
  border: 1px solid #d1d0d050;
  box-sizing: border-box;
}

/* 红色的周末和祝日 */
.sunday,
.saturday{
  background-color: #fdd;
  border: 1px solid #d1d0d050;
  color: black;
}

/* 黄色的今天 */
.today {
  background-color: #ffff99;
  border: 1px solid #d1d0d050;
}

.holiday {
  color: red;
}

</style>