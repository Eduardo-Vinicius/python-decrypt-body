#!/bin/bash

NAME=$1
SITE_PACKAGES=$(pipenv --venv)/lib/python3.8/site-packages
echo "Library Location: $SITE_PACKAGES"
DIR=$(pwd)

echo "executing pipenv install"
pipenv install --system --deploy

BUILD_PATH="build"
PACKAGE="package.zip"
mkdir -p $BUILD_PATH

echo $PACKAGE

rm $BUILD_PATH/$PACKAGE

echo "zipping package file"

cd $SITE_PACKAGES
zip -r9 $DIR/$BUILD_PATH/$PACKAGE *

cd $DIR
zip -g $BUILD_PATH/$PACKAGE main.py
zip -r $BUILD_PATH/$PACKAGE app

AWS_PROFILE=$AWS_PROFILE
if [ -z $AWS_PROFILE ]
then
    $AWS_PROFILE = "default"
fi

echo "done $BUILD_PATH/$PACKAGE"

echo "AWS lambda deploying package $BUILD_PATH/$PACKAGE"

echo $(aws lambda update-function-code --function-name $NAME --zip-file fileb://build/package.zip --profile $AWS_PROFILE)

echo "done AWS lambda $NAME deployed package $BUILD_PATH/$PACKAGE"