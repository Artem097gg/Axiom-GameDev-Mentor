PHYSICS_LESSON = (
    "🍎 **Unit: The Physics Engine (PhysX)**\n\n"
    "Unity uses the NVIDIA PhysX engine to simulate real-world forces. To build stable systems, you must understand:\n\n"
    "1️⃣ **Rigidbody Management:** Never move physics objects via `Transform.position`. Always use `Rigidbody.AddForce()` to stay consistent with the simulation.\n"
    "2️⃣ **FixedUpdate vs Update:** Physics is calculated on a fixed timer (0.02s). All physics-related code MUST live in `FixedUpdate()` to avoid jittering.\n"
    "3️⃣ **Colliders:** Primitive shapes (Box, Sphere) are mathematically optimized. Use them instead of Mesh Colliders whenever possible for high performance.\n\n"
    "📖 **Official Documentation:** [Rigidbody Component](https://docs.unity3d.com/Manual/class-Rigidbody.html)"
)
