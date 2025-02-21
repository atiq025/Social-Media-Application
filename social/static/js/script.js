setTimeout(() => {
    document.querySelectorAll('.fade-out').forEach(message => {
        message.style.transition = 'opacity 1s ease';
        message.style.opacity = '0';
        setTimeout(() => message.style.display = 'none', 1000); // Wait for fade-out to complete
    });
}, 1500);