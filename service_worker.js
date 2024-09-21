self.addEventListener('install', function(event) {
    // インストール時の処理
    self.skipWaiting();
  });
  
  self.addEventListener('activate', function(event) {
    // アクティブ化時の処理
    event.waitUntil(
      caches.keys().then(function(cacheNames) {
        return Promise.all(
          cacheNames.map(function(cacheName) {
            if (cacheName.startsWith('v')) {
              return caches.delete(cacheName);
            }
          })
        );
      })
    );
  });