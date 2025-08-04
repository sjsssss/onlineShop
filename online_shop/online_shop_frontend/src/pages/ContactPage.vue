<template>
  <div class="home-container">

    <div class="contact-container">
        <h2 class="title">お問い合わせ</h2>
        <p class="description">
        以下のフォームの項目を入力し、よろしければ「この内容で問い合わせる」ボタンをクリックしてください。
        </p>
        <p class="note">
        ※基本的に2〜3営業日で返信しておりますが、内容によっては返信にお時間がかかる場合がございます。ご了承ください。
        </p>

        <form class="contact-form" @submit.prevent="submitForm">
        <div class="form-row">
            <label>お名前 <span class="required">必須</span></label>
            <input type="text" v-model="name" required />
        </div>

        <div class="form-row">
            <label>メールアドレス <span class="required">必須</span></label>
            <input type="email" v-model="email" required />
        </div>

        <div class="form-row">
            <label>お問い合わせ内容 <span class="required">必須</span></label>
            <textarea v-model="message" rows="6" maxlength="2000" required></textarea>
            <p class="char-limit">※全角2000文字まで</p>
        </div>

        <div class="form-actions">
            <button type="submit">この内容で問い合わせる</button>
        </div>
        </form>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'

const name = ref('')
const email = ref('')
const message = ref('')

const submitForm = () => {
  if (!name.value || !email.value || !message.value) {
    alert('すべての必須項目を入力してください。')
    return
  }

  // 示例提交逻辑：后续可替换为API调用
  alert('送信が完了しました。ありがとうございました！')
}
</script>

<style scoped>
.home-container {
  display: flex;
  padding: 20px 60px;
  gap: 24px;
  background: #f1e7cb;
}
.contact-container {
  max-width: 700px;
  margin: 0 auto;
  padding: 30px;
  background: #f1e7cb;
}

.title {
  font-size: 22px;
  font-weight: bold;
  margin-bottom: 16px;
}

.description,
.note {
  font-size: 14px;
  color: #555;
  margin-bottom: 8px;
}

.contact-form {
  margin-top: 20px;
}

.form-row {
  display: flex;
  flex-direction: column;
  margin-bottom: 20px;
}

.form-row label {
  font-weight: bold;
  margin-bottom: 6px;
}

.required {
  background-color: #e60000;
  color: white;
  font-size: 12px;
  padding: 2px 6px;
  border-radius: 3px;
  margin-left: 8px;
}

input,
textarea {
  padding: 10px;
  font-size: 14px;
  border: 1px solid #ccc;
  border-radius: 4px;
  width: 100%;
}

.char-limit {
  font-size: 12px;
  color: #888;
  margin-top: 4px;
}

.form-actions {
  text-align: center;
  margin-top: 20px;
}

button {
  background-color: #666;
  color: white;
  border: none;
  padding: 12px 24px;
  font-size: 14px;
  border-radius: 4px;
  cursor: pointer;
}

button:hover {
  background-color: #444;
}
</style>
