#include "Model.as"
#include "Camera.as"
#include "Skins.as"

shared class SoccerBallModel : Model
{
	Object@ object;

	SoccerBallModel(Object@ object, float scale = 0.25f)
	{
		super(scale * 8);
		@this.object = object;

		AddSegment("ball", ModelSegment("SoccerBall.obj", "Colors.png"));
	}

	void PreRender()
	{
		Model::PreRender();
		Matrix::SetTranslation(matrix, object.interPosition.x, object.interPosition.y, object.interPosition.z);
		Matrix::SetRotationDegrees(matrix, -object.interRotation.x, -object.interRotation.y, -object.interRotation.z);
	}
}