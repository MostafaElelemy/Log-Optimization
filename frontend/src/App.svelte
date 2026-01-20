<script>
  import { onMount } from 'svelte';

  let logs = [];
  let newRawContent = '';
  let source = 'Web Server 01';

  // دالة لسحب البيانات من الـ API
  async function fetchLogs() {
    const res = await fetch('http://127.0.0.1:8000/api/logs/');
    logs = await res.json();
  }

  // دالة لإرسال Log جديد
  async function submitLog() {
    await fetch('http://127.0.0.1:8000/api/logs/', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ source, raw_content: newRawContent })
    });
    newRawContent = '';
    fetchLogs(); // تحديث القائمة
  }

  onMount(fetchLogs);
</script>

<main style="font-family: sans-serif; padding: 20px; background: #f4f7f6; min-height: 100vh;">
  <h1 style="color: #2c3e50;">LogSquash Pro Dashboard</h1>
  
  <div style="background: white; padding: 20px; border-radius: 8px; margin-bottom: 20px; box-shadow: 0 2px 10px rgba(0,0,0,0.1);">
    <h3>Compress New Logs</h3>
    <input bind:value={source} placeholder="Source (e.g. Server Name)" style="width: 100%; padding: 10px; margin-bottom: 10px;"/>
    <textarea bind:value={newRawContent} placeholder="Paste your messy logs here..." rows="5" style="width: 100%; padding: 10px;"></textarea>
    <button on:click={submitLog} style="background: #e74c3c; color: white; border: none; padding: 10px 20px; border-radius: 5px; cursor: pointer; margin-top: 10px;">
      Squash Logs!
    </button>
  </div>

  <div style="display: grid; grid-template-columns: repeat(auto-fill, minmax(300px, 1fr)); gap: 20px;">
    {#each logs as log}
      <div style="background: white; border-left: 5px solid #2ecc71; padding: 15px; border-radius: 5px; box-shadow: 0 2px 5px rgba(0,0,0,0.05);">
        <strong style="color: #7f8c8d;">Source: {log.source}</strong>
        <p style="margin: 10px 0;"><strong>Reduction:</strong> <span style="color: #27ae60;">{log.reduction_percentage}%</span></p>
        <div style="font-size: 12px; background: #eee; padding: 5px; max-height: 100px; overflow-y: auto;">
          <pre>{log.compressed_content}</pre>
        </div>
        <small style="color: #bdc3c7;">Size: {log.original_size}B -> {log.compressed_size}B</small>
      </div>
    {/each}
  </div>
</main>