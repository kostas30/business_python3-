 (cd "$(git rev-parse --show-toplevel)" && git apply --3way <<'EOF' 
diff --git a/code/code.py b/code/code.py
index e82175e392e88ea3332ae7378c8ad7aca9a62e78..5e10ba366a6c96bc437d8d94de6542fc1c6e3149 100644
--- a/code/code.py
+++ b/code/code.py
@@ -1,27 +1,29 @@
 import time
 
 
 class First:
-	def __int__(self, one, two):
-		self.one = one
-		self.two = two
-		self.now()
-
-	def now(self):
-		timer1 = time.time()
-		# print(f"{timer1:.2f}")
-		time.sleep(2.2)
-		timer2 = time.time()
-		# print(f"{timer2:.2f}")
-		time.sleep(2.2)
-		timer3 = time.time()
-		# print(f"{timer3:.2f}")
-		return timer1, timer2, timer3
+    """Simple timer that records three timestamps."""
+
+    def __init__(self, pause_between_measurements: float = 2.2) -> None:
+        """Store the pause duration and optionally take an initial reading."""
+        self.pause_between_measurements = pause_between_measurements
+        self.now()
+
+    def now(self):
+        timer1 = time.time()
+        # print(f"{timer1:.2f}")
+        time.sleep(self.pause_between_measurements)
+        timer2 = time.time()
+        # print(f"{timer2:.2f}")
+        time.sleep(self.pause_between_measurements)
+        timer3 = time.time()
+        # print(f"{timer3:.2f}")
+        return timer1, timer2, timer3
 
 
 class Second:
-	pass
+    pass
 
 
 a = First()
 print(a.now())
 
EOF
)
