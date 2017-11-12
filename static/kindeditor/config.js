//config.js
KindEditor.ready(function (K) {
    // K.create('textarea[name=content]', {
    K.create('textarea[name=content]', {
        width: '1000px',
        height: '1000px',
        uploadJson: '/admin/upload/images',
    });
});