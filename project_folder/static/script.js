// إضافة مؤشرات تفاعلية
document.querySelectorAll('input, select').forEach(element => {
    element.addEventListener('focus', () => {
        element.parentElement.style.transform = 'scale(1.02)';
    });
    
    element.addEventListener('blur', () => {
        element.parentElement.style.transform = 'scale(1)';
    });
});

// إرسال النموذج مع تأثيرات
document.getElementById('attendanceForm').addEventListener('submit', function(e) {
    e.preventDefault();
    const button = document.querySelector('.glow-button');
    
    // تأثير التحميل
    button.innerHTML = '<i class="fas fa-spinner fa-spin"></i> جاري التسجيل...';
    button.style.opacity = '0.7';
    
    // محاكاة الإرسال (استبدل بالكود الحقيقي)
    setTimeout(() => {
        button.innerHTML = '<i class="fas fa-check"></i> تم التسجيل!';
        button.style.background = '#4CAF50';
        
        // إعادة تعيين النموذج بعد 2 ثانية
        setTimeout(() => {
            this.reset();
            button.innerHTML = '<i class="fas fa-paper-plane"></i> تأكيد الحضور';
            button.style.background = 'linear-gradient(45deg, #007bff, #6610f2)';
            button.style.opacity = '1';
        }, 2000);
    }, 1500);
});