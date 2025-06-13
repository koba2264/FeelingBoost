const chatBox = document.getElementById('chatBox');
const expandBtn = document.getElementById('expandBtn');
let isExpanded = false;

expandBtn.addEventListener('click', () => {
  if (!isExpanded) {
    chatBox.style.position = 'fixed';
    chatBox.style.top = '90px';
    chatBox.style.left = '50%';
    chatBox.style.transform = 'translateX(-50%)';
    chatBox.style.width = '90%';
    chatBox.style.height = '80vh';
    chatBox.style.maxHeight = 'none';
    chatBox.style.zIndex = '2000';
    chatBox.style.backgroundColor = '#fff';
    chatBox.style.boxShadow = '0 0 10px rgba(0,0,0,0.3)';

    expandBtn.style.position = 'fixed';
    expandBtn.style.top = '95px';
    expandBtn.style.right = '30px';
    expandBtn.src = "/static/main/close.png";

    isExpanded = true;
  } else {
    chatBox.removeAttribute('style');
    expandBtn.removeAttribute('style');
    expandBtn.className = 'expand-icon';
    expandBtn.src = "/static/main/up.png";

    isExpanded = false;
  }
});
