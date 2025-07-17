class Test : MUSH::AsBehaviour
{
    int gObjHandle;
    float deltaTime;

    void Init(int gObjHandle)
    {
        this.gObjHandle = gObjHandle;
    }

    void OnActive()
    {

    }

    void EarlyUpdate()
    {
        deltaTime = MUSH::GetDeltaTime();
    }

    void Update()
    {

    }

    void LateUpdate()
    {
        MUSH::Rotate(gObjHandle, 0.1f*deltaTime, 0, 0);
    }
}