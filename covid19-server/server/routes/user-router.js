import express from 'express';
import * as userController from '../controllers/users-controller';
var router = express.Router();

/* GET users listing. */
router.route('/users/:id')
  .get(userController.get);

router.route('/users')
  .get(userController.list)
  .post(userController.save);

export default router;
